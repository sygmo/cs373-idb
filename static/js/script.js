$(document).ready(function(){
				$('#sortableTable').dataTable({
					"bFilter": false
                 });
			});

			
$(function() {
    $('#btn').click(function() {
		var param = "search";
        var query = {"search" : $('#srch').val()};
        $.ajax({
            type: 'GET',
			url: "/search",
			cache: false,
            data: query,
			datatype: "jsonp",
            success: function(response) {
                console.log(response);
            }
        });
    });
});

