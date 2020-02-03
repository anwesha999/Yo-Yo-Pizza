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
                    content: 'Hello, I am Mona, Mona Darling',
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
                messageReceived: false
            },
            displayHeader:true,
            currentState:"start"
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
            this.processUserResponse(message.content)
            console.log(message.content)

            this.messages.push(message);

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
        processUserResponse:function(message){
            switch(this.currentState){
                case "start"    : 
                    console.log("start")
                    if (message == 1){
                        this.currentState="pizza-selection"
                    }
                    else if (message == 2){
                        this.currentState="orderStatus"
                    }
                    else{
                        this.notAppropriateResponse()
                    }
                    break;
                case "pizza-selection" :
                    console.log("pizza-selection")
                    break;
                default:

            }
            this.sendUserMessage()
        },
        notAppropriateResponse:function(){
            var message = {
                        content: 'Your Response was not recognized please responsond correctly.',
                        myself: false,
                        participantId: 1,
                        timestamp: moment()
                    }
            // this.toLoad.push(message)
            this.messages.push(message)
        },
        sendUserMessage:function(){
            switch(this.currentState){
                case "pizza-selection":
                    var message = {
                                content: 'Please select a Pizza  \n\n1. Margereta \n\n2.Farmhouse \n\n3.Corn and Cheeze \n\n4. 5-Layer Cheeze Burst',
                                myself: false,
                                participantId: 1,
                                timestamp: moment()
                            }
                    // this.toLoad.push(message)
                    this.messages.push(message)
                default:
                    console.log("Reached Default case")
            }
        }
    }
}
</script>
<style scoped>
#chat-container{
    height:98vh;
}
</style>