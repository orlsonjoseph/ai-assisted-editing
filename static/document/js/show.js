
// When the document is ready, create a new Quill instance and set the theme to 'snow'
$(document).ready(function () {
    const requestURL = $('#editor').data('url');
    const csrftoken = Cookies.get('csrftoken');

    var quill = new Quill('#editor', {
        theme: 'snow'
    });

    quill.on('text-change', function (operations, content, source) {
        if (source === 'api') return;

        let formData = new FormData();

        formData.append('operations', JSON.stringify(operations));
        formData.append('content', JSON.stringify(content));

        formData.append('csrfmiddlewaretoken', csrftoken);

        customRequest(requestURL, formData, function (json) {
            console.log(json);
        });
    });

    // Get the document content from the server
    let content = $('#server-content').val();
    quill.setContents(content, 'api');
});
