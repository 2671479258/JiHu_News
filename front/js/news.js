var vm3 = new Vue({
    el: '#app3',
    data: {
        host: 'http://127.0.0.1:8000',
        newsRecords: [],
        articlesRecords: [],
        NewsContent: {},
        VideoRecords:[]
    },

    mounted: function () {
        this.get_news();
    },

    methods: {
        get_news: function () {
            var url = this.host + '/get_news/';
            axios.get(url, {
                responseType: 'json',
                withCredentials: true,
            })
            .then(response => {
                this.newsRecords = response.data.Nrecords;
                this.articlesRecords = response.data.Arecords;
                this.VideoRecords=response.data.Vrecords;
            })
            .catch(error => {
                status = error.response.status;
                if (status == 401 || status == 403) {
                    location.href = '127.0.0.1:8080/index.html';
                } else {
                    // alert(error.response.data.detail);
                }
            });
        },


    }
});