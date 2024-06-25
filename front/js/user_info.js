var vm6 = new Vue({
    el: '#app6',
    data: {
        host: 'http://127.0.0.1:8000',
        UserInfo: '',
        username: getCookie('username'),
    },
    mounted: function () {
        this.get_info();
    },
    methods: {
          get_info: function () {
        var url = this.host + '/get_userinfo/';
        axios.get(url, {
            responseType: 'json',
            params: {
                username: this.username,
            },
            withCredentials: true
        })
        .then(response => {
            this.UserInfo = response.data.userinfo;
            // 更新头像 URL，添加时间戳以确保重新加载
            this.UserInfo.profile += `?timestamp=${new Date().getTime()}`;
        });
    },


        handleAvatarUpload: function (event) {
            var formData = new FormData();
            formData.append('avatar', event.target.files[0]);
            axios.post(this.host + '/upload_avatar/', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data'
                },
                    withCredentials: true
            })
            .then(response => {
                console.log(response.data.message);
                window.location.reload(); // 重新加载当前页面

                // 可以根据返回的信息进行一些提示或者处理
            })
            .catch(error => {
                console.error('Error uploading avatar:', error);
            });
        }
    }
});