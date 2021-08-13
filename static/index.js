// calculate
$('#calc').click(function () {
    var targetUrl = $("#form").attr("action");
    var data = new FormData($("#form")[0])
    $.ajax({
        type: "POST",
        url: targetUrl,
        cache: false,
        processData: false,
        contentType: false,
        data: data,
        dataType: "json",
        success: function (res) {
            console.log(res)
            $('#res').val(res.c)
        },
        error: function (err) {
            console.log(err)
        }
    })
})
// clear
$('#clear').click(function () {
    $('#a').val('')
    $('#b').val('')
    $('#res').val('')
})