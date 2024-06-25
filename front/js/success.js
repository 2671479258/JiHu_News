function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);

    if (parts.length === 2) {
        return parts.pop().split(';').shift();
    }
}

var vm2 = new Vue({
    el: '#app2',
    delimiters: ['[[', ']]'],
    data: {
        host,
        username: getCookie('username'),
        profileUrl: '',  // 添加一个属性用于保存用户头像链接
    },
    mounted() {
        console.log('Created hook - Cookie username:', this.username);
        // 发送 AJAX 请求获取当前登录用户的头像链接
        axios.get(this.host + '/get_profile/', {
            withCredentials: true,

        })
        .then(response => {
            // 将获取到的头像链接赋值给 profileUrl
            this.profileUrl = response.data.profile;
        })
        .catch(error => {
            console.log(error.response);
        });
    },
    methods: {
        logoutfunc: function () {
            var url = this.host + '/logout/';
            axios.delete(url, {
                responseType: 'json',
                withCredentials:true,
            })
                .then(response => {
                    location.href = 'index.html';
                })
                .catch(error => {
                    console.log(error.response);
                })
        },
    }
});