<template>
  <div id="AddEvent">
    <h2> Create Your Event </h2>
        <form>
            <label>Title:</label>
            <input type = "text" v-model.lazy="event.title" required/>
            <label>Capacity:</label>
            <input type = "number" v-model.lazy="event.capacity" required/>
            <label>Time:</label>
            <input type = "number" v-model.lazy="event.time" required/>
            <label>Location:</label>
            <input type = "text" v-model.lazy="event.location" required/>
            <label>Event Information </label>
            <textarea v-model.lazy="event.info"></textarea>   
    
        </form>
        <div id = "preview">
            <h3>Preview Event</h3>
            <p>Title: {{event.title}}</p>
            <p>Capacity: {{event.capacity}}</p>
            <p>Time: {{event.time}}</p>
            <p>Location: {{event.location}}</p>
            <p>Event Information:</p>
            <p>{{event.info}}</p>
        </div>
    </div>
</template>

<script>


export default {

    data() {
        return{
            event:{
                title: "",
                capacity: "",
                time: "",
                ocation: "",
                info: ""
            }
        }
    },
    methods: {

    }
}
</script>

<style>
#AddEvent *{
    box-sizing: border-box;
}
#AddEvent{
    margin: 20px auto;
    max-width: 500px;
}
label{
    display: block;
    margin: 20px 0 10px;
}
input[type="text"],textarea{
    display:block;
    width: 100%;
    padding: 8px;
}
#preview{
    padding: 10px 20px;
    border: 1px dotted #ccc;
    margin: 30px 0;
}
h3{
    margin-top: 10px;
}





</style>