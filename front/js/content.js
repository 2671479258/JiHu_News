var vm = new Vue({
    el: '#app',
    data: {
        host: 'http://127.0.0.1:8000',  // 请确保与后端API的地址匹配
        user_id: '',
        NewsContent: [],
    },
    mounted: function () {
        // 获取cookie中的用户名
        this.username = getCookie('username');
        // 获取用户ID
        this.user_id = sessionStorage.user_id || localStorage.user_id;

        // 假设你有一个新闻的ID，这里使用1作为示例
        var new_id = 1;
        this.newsContent(new_id);
    },
    methods: {
        newsContent: function (new_id) {
            var url = this.host + '/new_content/' + new_id + '/';
            console.log("Request URL:", url);

            axios.get(url, {
                responseType: 'json',
                withCredentials: true, // 根据需要设置是否需要发送凭据（比如 Cookie）
            })
            .then(response => {
                this.NewsContent = response.data.records;
            })
            .catch(error => {
                console.error("Error:", error);
                // 处理错误
            });
        },
    }
});