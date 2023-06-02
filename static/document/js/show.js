
// When the document is ready, create a new Quill instance and set the theme to 'snow'
$(document).ready(function () {
    const updateURL = $('#editor').data('url-update');
    const showURL = $('#editor').data('url-show');

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

        customRequest(updateURL, formData, function (json) {
            console.log(json);
        });
    });

    // Get the document content from the server
    let formData = new FormData();
    formData.append('csrfmiddlewaretoken', csrftoken);

    customRequest(showURL, formData, function (content) {
        quill.setContents(JSON.parse(content), 'api');
    });
});
