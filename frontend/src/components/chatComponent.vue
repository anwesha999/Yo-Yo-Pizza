<template>
    <div id="chat-container">
      <Chat 
       :participants="participants"
       :myself="myself"
       :messages="messages"
       :onType="onType"
       :loadMoreMessages="loadMoreMessages"
       :onMessageSubmit="onMessageSubmit"
       :chatTitle="chatTitle"
       :placeholder="placeholder"
       :colors="colors"
       :borderStyle="borderStyle"
       :hideCloseButton="hideCloseButton"
       :closeButtonIconSize="closeButtonIconSize"
       :submitIconSize="submitIconSize"/>
   </div>
</template>
<script>
import {Chat} from 'vue-quick-chat';
import 'vue-quick-chat/dist/vue-quick-chat.css';
import moment from 'moment'
import axios from "axios"

export default {
    components: {
        Chat
    },
    data() {
        return {
            visible: true,
            participants: [
                {
                    name: 'YO YO Pizza',
                    id: 1
                }
            ],
            myself: {
                name: 'Anonymous',
                id: 2
            },
            messages: [
                {
                    content: 'Hello, I am Mona!',
                    myself: false,
                    participantId: 1,
                    timestamp: moment()
                },
                {
                    content: 'I will be assisting you here',
                    myself: false,
                    participantId: 1,
                    timestamp: moment()
                },
                {
                    content: '\nHow can I help you? \n\n1. Place a New Order \n\n2. Get Order Status',
                    myself: false,
                    participantId: 1,
                    timestamp: moment()
                }

            ],
            chatTitle: 'YO Yo Pizza Order',
            placeholder: 'Please Write something',
            colors: {
                header: {
                    bg: '#d30303',
                    text: '#fff'
                },
                message: {
                    myself: {
                        bg: '#fff',
                        text: '#bdb8b8'
                    },
                    others: {
                        bg: '#fb4141',
                        text: '#fff'
                    },
                    messagesDisplay: {
                        bg: '#f7f3f3'
                    }
                },
                submitIcon: '#b91010'
            },
            borderStyle: {
                topLeft: "10px",
                topRight: "10px",
                bottomLeft: "10px",
                bottomRight: "10px",
            },
            hideCloseButton: false,
            submitIconSize: "30px",
            closeButtonIconSize: "20px",
            asyncMode: true,
            toLoad: [
            ],
            scrollBottom: {
                messageSent: true,
                messageReceived: true
            },
            displayHeader:true,
            nextState:"showMenu",
            requestData: {
                name:null,
                pizzaVariety:null,
                amount:null,
                address:null,
                phoneNumber:null,
                placedAt:null
            },
            menu:{
                1:{
                    name:"Margereta",
                    price:100
                },
                2:{
                    name:"Farmhouse",
                    price:125
                },
                3:{
                    name:"Corn and Cheeze",
                    price:125
                },
                4:{
                    name:"5-Layer Cheeze Burst",
                    price:150
                }
            },
            incorrectResponse:'Your Response was not recognized please responsond correctly.',
            uid : ""
        }
    },
    methods: {
        onType: function (event) {
            //here you can set any behavior
        },
        loadMoreMessages(resolve) {
            setTimeout(() => {
                resolve(this.toLoad); //We end the loading state and add the messages
                //Make sure the loaded messages are also added to our local messages copy or they will be lost
                this.messages.unshift(...this.toLoad);
                this.toLoad = [];
            }, 1000);
        },
        onMessageSubmit: function (message) {
            /*
            * example simulating an upload callback. 
            * It's important to notice that even when your message wasn't send 
            * yet to the server you have to add the message into the array
            */

            this.messages.push(message);

            
            this.processUserResponse(message.content)

            /*
            * you can update message state after the server response
            */
            // timeout simulating the request
            setTimeout(() => {
                message.uploaded = true
            }, 2000)
        },
        onClose() {
            this.visible = false;
        },
        saveUserToDB:function(){
            axios({
                method: 'post',
                url: "http://127.0.0.1:5000/user_info",
                data: {
                    name:this.requestData.name,
                    address:this.requestData.address,
                    phoneNumber:this.requestData.phoneNumber
                },
                headers : {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin' : '*'
                }
            });
        },
        placeOrder : function(){
            var req = axios({
                method: 'post',
                url: "http://127.0.0.1:5000/place_order",
                data: {
                    pizzaVariety:this.requestData.pizzaVariety,
                    amount:this.requestData.amount,
                    phoneNumber:this.requestData.phoneNumber,
                    placedAt:this.requestData.placedAt
                },
                headers : {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin' : '*'
                }
            });
            Promise.resolve(req).then(uid => {
                this.uid = uid.data
                this.processUserResponse("")
            })
        },
        processUserResponse:function(message){
            message = message.trim()
            switch(this.nextState){
                case "showMenu"    : 
                    if (message == 1){
                        var msg = 'Please select a Pizza  \n\n1. Margereta \n\n2.Farmhouse \n\n3.Corn and Cheeze \n\n4. 5-Layer Cheeze Burst'
                        this.sendMessage(msg)
                        this.nextState="pizzaSelected"
                    }
                    else if (message == 2){
                        this.nextState="orderStatus"
                    }
                    else{
                        this.sendMessage(this.incorrectResponse)
                    }
                    break;
                case "pizzaSelected" :
                    if(this.menu[message] !== undefined){
                        var obj = this.menu[message]
                        this.requestData.pizzaVariety = obj.name
                        this.requestData.amount = obj.price
                        var msg = "You have selected "+obj.name+" which cost "+obj.price
                        this.sendMessage(msg)
                        this.sendMessage("Please tell me you name.")
                        this.nextState="user-name"
                    }
                    else{
                        this.sendMessage(this.incorrectResponse)
                    }
                    break;
                case "user-name":
                    this.myself.name = message
                    this.requestData.name = message
                    var msg = "Nice to meet you " + message 
                    this.sendMessage(msg)
                    this.sendMessage("Please tell me your mobile number.")
                    this.nextState = "user-mobile"
                    break;
                case "user-mobile":
                    this.requestData.phoneNumber = message
                    this.sendMessage("Thank You for providing your mobile number.")
                    this.sendMessage("Please tell me where we need to deliver pizza.")
                    this.sendMessage("What is your address?")
                    this.nextState = "user-address"
                    this.saveUserToDB()
                    break;
                case "user-address":
                    this.requestData.address = message
                    this.requestData.placedAt = moment().unix()
                    this.saveUserToDB()
                    this.placeOrder()
                    this.nextState = "finish"
                    break;
                case "finish":
                    var msg = [
                        "Thank you for provinding your address.",
                        "We will be delivering your pizza within 30 mins.",
                        "Your Order ID is "+this.uid,
                        "Please keep it for further refrence."
                    ]
                    msg.forEach(element => {
                        this.sendMessage(element)
                    });
                    this.nextState = "end"
                    break
                case "end":
                    this.sendMessage("You order will be delivered shortly.")
                    break;
                default:
                    pass
            }
        },
        sendMessage(msg){
            var message = {
                        content: msg,
                        myself: false,
                        participantId: 1,
                        timestamp: moment()
                    }
            this.messages.push(message)
        }
    }
}
</script>
<style scoped>
#chat-container{
    height:96vh;
}
</style>