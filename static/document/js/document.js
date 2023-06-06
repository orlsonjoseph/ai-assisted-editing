$(document).ready(function () {
    const updateURL = $('#editor').data('url-update'),
        csrftoken = Cookies.get('csrftoken'),
        prefix = $(document).prop('title').split('|')[0];

    let previousDocumentTitle = null;


    $('#title').on('focus', function () {
        previousDocumentTitle = $(this).text();
    }).on('blur', function () {
        let newDocumentTitle = $(this).text()

        if (newDocumentTitle === '') {
            // Restore previous title
            $(this).text(previousDocumentTitle);
            return;
        }

        newDocumentTitle = newDocumentTitle.trim();

        // Send update request to server
        let formData = new FormData();

        formData.append('title', newDocumentTitle);
        formData.append('csrfmiddlewaretoken', csrftoken);

        customRequest(updateURL, formData, function (json) {
            // Update page title
            $(document).prop('title', prefix + ' | ' + newDocumentTitle);
        });
    });
});