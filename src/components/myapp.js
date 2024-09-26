new Vue({
    el:'#myApp',
    data: {
        event: {},
        addedEvent: {}  
    },
    methods: {
        addEvent: function() {
            this.addedEvent.push(event);
            this.cleanEvent();
        },
        cleanEvent: function() {
            this.event = {}
        }
    }
})