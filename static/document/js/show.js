
// When the document is ready, create a new Quill instance and set the theme to 'snow'
$(document).ready(function () {
    const editURL = $('#editor').data('url-edit');
    const showURL = $('#editor').data('url-show');

    const csrftoken = Cookies.get('csrftoken');
    let selectedText = null;

    var quill = new Quill('#editor', {
        theme: 'snow'
    });

    quill.on('text-change', function (operations, content, source) {
        if (source === 'api') return;

        var formData = new FormData();

        formData.append('operations', JSON.stringify(operations));
        formData.append('content', JSON.stringify(content));

        formData.append('csrfmiddlewaretoken', csrftoken);

        customRequest(editURL, formData, function (json) {
            console.log(json);
        });
    });

    const offset = 10;

    quill.on('selection-change', function (range) {
        let highlight = $('#highlight'), highlightStatus = highlight.is(':visible');

        if (!range || range.length == 0) {
            if (highlightStatus) highlight.hide();

            return;
        }

        let bounds = quill.getBounds(range.index, range.length);
        let editorCoordinates = $('#editor').offset();

        selectedText = quill.getText(range.index, range.length);

        // Open highlight menu at the bounds
        highlight.css({
            top: editorCoordinates.top + bounds.top - highlight.outerHeight() - offset,
            left: editorCoordinates.left + bounds.left - (highlight.width() / 2) + (bounds.width / 2),
        }).show();

    });

    $('#highlight ul li[data-fx="rephrase"]').on('click', function () {
        var apiURL = $(this).data('url'), formData = new FormData();

        formData.append('content', selectedText);
        formData.append('csrfmiddlewaretoken', csrftoken);

        customRequest(apiURL, formData, function (json) {
            console.log(json);
        });
    });

    // Get the document content from the server
    var formData = new FormData();
    formData.append('csrfmiddlewaretoken', csrftoken);

    customRequest(showURL, formData, function (content) {
        quill.setContents(JSON.parse(content), 'api');
    });
});
