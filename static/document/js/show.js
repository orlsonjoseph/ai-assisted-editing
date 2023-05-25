
// When the document is ready, create a new Quill instance and set the theme to 'snow'
$(document).ready(function () {
    const requestURL = $('#editor').data('url');
    const csrftoken = Cookies.get('csrftoken');

    var quill = new Quill('#editor', {
        theme: 'snow'
    });

    // Listen to the 'text-change' event and send AJAX request to the server
    // delta: changes made to the document
    // state: state of the document before the change
    // source: source of the change

    quill.on('text-change', function (delta, state, source) {
        let formData = new FormData();

        formData.append('delta', JSON.stringify(delta));
        formData.append('state', JSON.stringify(state));

        formData.append('csrfmiddlewaretoken', csrftoken);

        customRequest(requestURL, formData, function (json) {
            console.log(json);
        });
    });
});
