var vm = new Vue({
    el: '#app',
    data: {
        host: host,
        username: '',
        password: '',
        remember: false
    },
    methods: {
        get_query_string: function (name) {
    var reg = new RegExp('(^|&)' + name + '=([^&]*)(&|$)', 'i');
    var r = window.location.search.substr(1).match(reg);
    if (r != null) {
        return decodeURI(r[2]);
    }
    return null;
},


        // 表单提交
        on_submit: function () {

            console.log(666)
            {

                axios.post(this.host + '/login/', {
                    username: this.username,
                    password: this.password,

                }, {
                    responseType: 'json',
                    // 发送请求的时候, 携带上cookie
                    withCredentials: true,
                    // crossDomain: true
                })
                    .then(response => {

                        if (response.data.code == 0) {
                            // 跳转页面
                            var return_url = this.get_query_string('next');
                            console.log('已到达')
                            if (!return_url) {
                                return_url = '/index.html';
                            }
                            location.href = return_url;
                        } else if (response.data.code == 400) {
                            this.error_pwd_message = '用户名或密码错误';
                             this.error_pwd = true;
                        }
                    })
                    .catch(error => {
                        if (error.response.status == 400) {
                            this.error_pwd_message = '用户名或密码错误';
                        } else {
                            this.error_pwd_message = '服务器错误';
                        }
                        this.error_pwd = true;
                    })
            }
        },

    }
});