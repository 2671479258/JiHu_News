var vm8 = new Vue({
    el: '#app111',
    delimiters: ['[[', ']]'],
    data: {
        host: host,
        username: sessionStorage.username || localStorage.username,
        user_id: sessionStorage.user_id || localStorage.user_id,
        token: sessionStorage.token || localStorage.token,
        page: 1,
        page_size: 5,
        count: 0,
        news: [], // Corrected property name
        query: '',

    },
    computed: {
        total_page: function() {
            return this.count; // This should probably return the actual total page count instead of 'count'
        },
        next: function() {
            if (this.page >= this.total_page) {
                return 0;
            } else {
                return this.page + 1;
            }
        },
        previous: function() {
            if (this.page <= 0) {
                return 0;
            } else {
                return this.page - 1;
            }
        },
        page_nums: function() {
            var nums = [];
            if (this.total_page <= 5) {
                for (var i = 1; i <= this.total_page; i++) {
                    nums.push(i);
                }
            } else if (this.page <= 3) {
                nums = [1, 2, 3];
            } else if (this.total_page - this.page <= 2) {
                for (var i = this.total_page; i > this.total_page - 5; i--) {
                    nums.push(i);
                }
            } else {
                for (var i = this.page - 2; i < this.page + 3; i++) {
                    nums.push(i);
                }
            }
            return nums;
        }
    },
    mounted: function() {
        this.username = getCookie('username');
        this.query = this.get_query_string('q');
        this.get_search_result();
    },
    methods: {
        logoutfunc: function() {
            var url = this.host + '/logout/';
            axios.delete(url, {
                    responseType: 'json',
                    withCredentials: true,
                })
                .then(response => {
                    location.href = 'login.html';
                })
                .catch(error => {
                    console.log(error.response);
                })
        },
        get_query_string: function(name) {
            var reg = new RegExp('(^|&)' + name + '=([^&]*)(&|$)', 'i');
            var r = window.location.search.substr(1).match(reg);
            if (r != null) {
                return decodeURI(r[2]);
            }
            return null;
        },
        get_search_result: function() {
            var url = this.host + '/search/';

            axios.get(url, {
                    params: {
                        q: this.query,
                        page: this.page,
                        page_size: this.page_size,
                    },
                    responseType: 'json',
                    withCredentials: true,
                })
                .then(response => {
                    this.news = response.data.list; // Corrected property name
                    this.count = response.data.count;
                    this.Q = this.query;
                    for (var i = 0; i < this.news.length; i++) { // Corrected property name
                        this.news[i].url = '/goods/' + this.news[i].id + ".html"; // Corrected property name
                    }
                })
                .catch(error => {
                    console.log(error);
                });
        },
        on_page: function(num) {
            if (num != this.page) {
                this.page = num;
                this.get_search_result();
            }
        },
        on_sort: function(ordering) {
            if (ordering != this.ordering) {
                this.page = 1;
                this.ordering = ordering;
                this.get_skus();
            }
        },
        getSearchKeyword: function() {
            this.query = document.getElementById('searchInput').value;
            this.get_search_result();
        }
    }
});