const api = '/api/fibonnaci'

function get_series() {
	const number = $('#number').val()
	if (number === '') {
		alert("Please enter number")
		return false
	}
	if (number.length > 6) {
		alert("Please enter number less than 6 digits")
		return false
	}
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "POST", api);
    xmlHttp.setRequestHeader('X-CSRFToken', $('input[name=csrfmiddlewaretoken]').val())
    xmlHttp.setRequestHeader('Accept', 'application/json')
    xmlHttp.setRequestHeader('Content-Type', 'application/json')
    xmlHttp.send( JSON.stringify({'number': number}) );
    update_series()
}

function update_series() {
    $.ajax({
        type: 'GET',
        url: api,
        success: function (response) {
        	let res = ''
        	for (let i = response.length - 1; i >= 0; i--) {
        		let row = response[i]
        		res += '<tr>'
        		res += '<td>' + row.number + '</td>'
        		res += '<td>' + row.fibonacci_series + '</td>'
        		res += '<td>' + row.runtime + '</td>'
        		res += '<td>' + row.created + '</td>'
        		res += '</tr>'
        	}
        	$('#data_S').html(res)
        },
    })
}