var vm777 = new Vue({
    el: '#app777',
    data: {
        host: 'http://127.0.0.1:8000',
        commentsRecords: [],
        userInput: '', // 用户输入的内容
        username: getCookie('username'),
        replyContent: '', // 回复内容
        replyMessage: '', // 回复提示信息
    },

    mounted: function () {
        this.newId = this.getNewIdFromUrl();
        this.get_comments();
    },

    methods: {
        getNewIdFromUrl: function () {
            var url = window.location.pathname;
            var parts = url.split('/');
            var newIdWithExtension = parts[parts.length - 1];
            var newId = newIdWithExtension.split('.')[0];
            return newId;
        },

        get_comments: function () {
            var url = this.host + '/get_comments/' + this.newId + '/';
            axios.get(url, {
                responseType: 'json',
                withCredentials: true,
            })
            .then(response => {
                this.commentsRecords = response.data.comments;
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

        checkAndPublish: function () {
            if (this.userInput.trim() === '') {
                alert('不能发表空内容！');
            } else {
                this.publishComment();
            }
        },

        publishComment: function () {
            var url = this.host + '/publish_comments/';
            axios.get(url, {
                responseType: 'json',
                params: {
                    comment: this.userInput,
                    username: this.username,
                    newId: this.newId,
                },
                withCredentials: true
            })
            .then(response => {
                console.log('评论发表成功');
                this.userInput = '';
                this.get_comments();
            })
            .catch(error => {
                console.error('发表评论失败:', error);
            });
        },

        showreply: function (comment) {
    var overlay = document.getElementById("overlay2-" + comment.id);
    overlay.style.display = "block";
    var rep = document.getElementById("reply-box-" + comment.id);
    rep.style.display = "block";
    this.replyContent = ''; // 清空回复内容
    this.replyMessage = '即将回复用户: ' + comment.username; // 设置提示信息
},



        closeReplyBox: function (id) {
    var overlay = document.getElementById("overlay2-" + id);
    var rep = document.getElementById("reply-box-" + id);
    var unlogin = document.getElementById("unlogin-" + id);
    var yeslogin = document.getElementById("yeslogin-" + id);
    overlay.style.display = "none";
    rep.style.display = "none";
    // unlogin.value = "";
    // yeslogin.value = "";
},



        submitReply: function (comment) {
    // 提交回复内容
    console.log('回复内容:', this.replyContent);

    this.closeReplyBox(comment.id); // 关闭遮罩和表单

    var url = this.host + '/publish_reply/';
    axios.get(url, {
        responseType: 'json',
        params: {
            reply: this.replyContent,
            username: this.username,
            receiver: comment.username,
            comment_id: comment.id
        },
        withCredentials: true
    })
    .then(response => {
        console.log('评论发表成功');
        alert('发送成功')
        this.replyContent = ''; // 清空回复内容

        this.get_comments(); // 更新评论列表
        location.reload(); // 原地刷新页面
    })
    .catch(error => {
        console.error('发表评论失败:', error);
    });
}



    }
});