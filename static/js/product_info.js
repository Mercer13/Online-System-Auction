
var data;

//get all user information 
$.ajax({
    url: "/product/rest/users/?format=json", success: function (result) {
        users = result;
        console.log(result);


    }, complete: function () {
        //do nothing 
    },

});


//get products  
console.log(id)

$("#load").click(function () {
    getproductinfo();
});
var finalmodal = 0;

function finalproduction() {
    if (data[0].bid != 0) {
        finalproduct()
    }
    else {

        alert("Помилка! Ви не можете продати товар!\nСтавки на даний товар відсутні...");
    }
}

function finalproduct() {
    //patch ajax call
    var x = {
        "status": 1,
    }

    var $crf_token = $('[name="csrfmiddlewaretoken"]').attr('value')
    $.ajax({
        type: "PATCH",
        url: "/product/rest/products/" + id + "/",
        csrfmiddlewaretoken: csrfToken,
        data: JSON.stringify(x),
        dataType: "json",
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            "X-CSRFToken": $crf_token,
            //content-type = application/x-www-form-urlencoded
        },
        success: function () {
            window.location.replace("/product/myproducts/");

        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {
            alert("some error " + String(errorThrown) + String(textStatus) + String(XMLHttpRequest.responseText));
        }
    });
}

function deleteproduct() {
    var $crf_token = $('[name="csrfmiddlewaretoken"]').attr('value')
    $.ajax({
        type: "DELETE",
        url: "/product/rest/products/" + id + "/",
        csrfmiddlewaretoken: csrfToken,
        //data : JSON.stringify(x),
        //dataType: "json",
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            "X-CSRFToken": $crf_token,
            //content-type = application/x-www-form-urlencoded
        },
        success: function () {
            window.location.replace("/product/myproducts/");

        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {
            alert("some error " + String(errorThrown) + String(textStatus) + String(XMLHttpRequest.responseText));
        }
    });
}



//function to change owner from url to name
function refresh() {
    for (var x in users) {
        if (users[x].url.includes(data[0].owner)) {
            data[0].owner = users[x].username
        }
    }


}

//Append products to html
function printResult() {

    console.log(currentUser, data[0].owner);
    if (currentUser == data[0].owner) {
        $("#bidInput").hide();
        $("#bid").hide();
        $('#contents').html('');
        $('#imageblock').html('');
        console.log(data[0].owner);
        console.log("button BID, INPUTE hide");

        for (var key in data) {
            if (data[key].bid != 0) {
                $("#contents").append('<h1><b>' + data[key].itemname + '</b></h1> <div>Опис: ' + data[key].description + '</div><div>Початкова ставка: ' + data[key].initialbid + ' грн</div><div>Дата початку: ' + data[key].createddate + '</div><div><h2>Теперішня ставка: ' + data[key].bid + 'грн</h2></div>');
                $('#imageblock').append('<img class="img-fluid justify-content-center" src="' + data[0].image + '">');
            }
            else {
                $("#contents").append('<h1><b>' + data[key].itemname + '</b></h1> <div>Опис: ' + data[key].description + '</div><div>Початкова ставка: ' + data[key].initialbid + ' грн</div><div>Дата початку: ' + data[key].createddate + '</div>');
                $('#imageblock').append('<img class="img-fluid justify-content-center" src="' + data[0].image + '">');
            }

        }


    }
    else {

        $('#contents').html('');
        $('#imageblock').html('');
        $('#final').hide();
        $('#abort').hide();
        console.log(data[0].owner);
        console.log("button ABORT, FINAL hide");
        for (var key in data) {

            if (data[key].bid != 0) {
                $("#contents").append('<h1><b>' + data[key].itemname + '</b></h1> <div>Опис: ' + data[key].description + '</div><div>Початкова ставка: ' + data[key].initialbid + ' грн</div><div> Дата створення: ' + data[key].createddate + '</div><div><h2>Теперішня ставка: ' + data[key].bid + ' грн</h2></div>');

                $('#imageblock').append('<img class="img-fluid img justify-content-center" src="' + data[0].image + '">');
            }
            else {
                $("#contents").append('<h1><b>' + data[key].itemname + '</b></h1> <div>Опис: ' + data[key].description + '</div><div>Початкова ставка: ' + data[key].initialbid + ' грн</div><div> Дата створення: ' + data[key].createddate + '</div>');

                $('#imageblock').append('<img class="img-fluid img justify-content-center" src="' + data[0].image + '">');
            }
        }

    }
}



function getproductinfo() {
    $.ajax({
        url: "/product/rest/products/?id=" + id + "&itemname=&owner=&status=&buyer=", success: function (result) {
            data = result;
            console.log(result + "-");



        }, complete: function () {

            refresh();
            if (data[0].length == 0) {
                window.location.replace("/product/");

            }
            else if (data[0].status == 1) {
                window.location.replace("/product/");

            }
            printResult();

        },

    });
}

function bidToProduct() {

    var bid = $('#bidInput').val()
    console.log(bid);
    if (bid < data[0].initialbid) {
        alert("value of bid must be greater than initial bid");
    }
    else if (bid < data[0].bid) {
        alert("value of your bid must be greater than current bid");
    }
    else if (bid > 999999) {
        alert("Занадто велике число!");
    }
    else {
        //patch ajax call
        var x = {
            "bid": bid,
            "buyer": currentUser,
            "status": 0,
        }

        var $crf_token = $('[name="csrfmiddlewaretoken"]').attr('value')
        $.ajax({
            type: "PATCH",
            url: "/product/rest/products/" + id + "/",
            csrfmiddlewaretoken: csrfToken,
            data: JSON.stringify(x),
            dataType: "json",
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                "X-CSRFToken": $crf_token,
                //content-type = application/x-www-form-urlencoded
            },
            success: function () {


            },
            error: function (XMLHttpRequest, textStatus, errorThrown) {
                alert("some error " + String(errorThrown) + String(textStatus) + String(XMLHttpRequest.responseText));
            }
        });
    }
}

$('#bid').click(function () {
    getproductinfo();
    bidToProduct();
    getproductinfo();

});


setInterval(getproductinfo, 100);


