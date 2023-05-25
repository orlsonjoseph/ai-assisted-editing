async function customRequest(url, data, callback) {
    await fetch(url, {
        method: 'POST', mode: 'same-origin',
        body: data, credentials: 'include'
    })
        .then(response => response.json())
        .then(json => callback(json))
        .catch(error => console.error('Error:', error));
}
