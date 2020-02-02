<template>
    <div id = "container">
        <div id = "message-history">

        </div>
        <div id = "send-message-box">
        </div>
    </div>
</template>
<script>
export default {
    name : "Chat",
    data() {
        return {  
            states : {
                start : "start",
                gettingOrderDetail : "Fectching Order Detail",
                confirmed : "confirmed",
                placed : "placed"
            }
        }
    },
    methods : {
        
    }
}
</script>
<style scoped>

#container{
    height: 98vh;
    /* border:1px solid black;
    border-radius: 5px; */
    /* background-color: aqua; */
}

#message-history{
    height:93vh;
    border:1px solid black;
    border-radius: 5px;
    /* background-color:bisque; */
}

#send-message-box{
    margin-top:5px;
    height:5vh;
    border:1px solid black;
    border-radius: 5px;
    /* background-color: brown */
}


</style>