$(document).ready(function () {
    $("#addItemForm").on("submit", function (e) {
        e.preventDefault();
        let data = new FormData($(this)[0]);

        console.log(data.get('image'))
        $.ajax({
            url: $(this).attr('action'),
            type:"POST",
            dataType: 'json',
            processData: false,
            contentType: false,
            data: data,
            success: function (response) {
                console.log('response')
                $("input:not([type=\"submit\"])").val("");
            },
            error: function (error) {
                console.log(error)
            }
        });
    });
});