// $(document).ready(() => {
//     $(document).on('submit', "form.search", function (event) {
//         event.preventDefault();
//         console.log("I am clicked!!!");
//         console.log("Url grabbed: ", $(this).attr('action'));
//         const cat = $('#category').val();
//         const q = $('#query').val();

//         $.ajax({
//             type: "get",
//             url: $(this).attr('action'),
//             data: {
//                 'catsel': cat,
//                 'q': q
//             },
//             dataType: "json",
//             success: function (response) {
//                 console.log(response);
//                 $(".search-div").html(response.search_data);
//             },
//             error: function (err) {
//                 console.log("Error occured");

//                 console.log(err.responseText);
//             }
//         });
//     })
// });

$(document).ready(() => {

  // Remove from wish-list
  $(document).on("submit", "form.remove-from-wish", function (event) {
    event.preventDefault();
    console.log("I am clicked!");
    const btn_id = $(this).attr("slug");

    $.ajax({
      type: "get",
      url: $(this).attr("action"),
      dataType: "json",
      success: function (response) {
        $(".wish-div").html(response.wish_item);
        $(".wish-list-div").html(response.wish_list);
        $(".cart-list-div").html(response.cart_list);
        $("#wish-from-detail").html(
          '<i class="fa fa-heart" aria-hidden="true"> Add to WishList</i>'
        );
        $("#wish-removed-alert")
          .html(`<div class="alert alert-danger alert-dismissible" role="alert">
        <button type="button" class="close" data-dismiss="alert" aria-label="Close">
          <span style="font-size: larger; color:black !important" aria-hidden="true">&times;</span>
        </button>
        <strong>Item Removed from the WishList!</strong>
      </div>`);
        setTimeout(() => {
          $("#wish-removed-alert").html(``);
        }, 4000);
      },
    });
  });

  // Remove from cart-list
  $(document).on("submit", "form.remove-from-cart", function (event) {
    event.preventDefault();
    console.log("I am clicked!");
    console.log($(this).attr("action"));

    $.ajax({
      type: "get",
      url: $(this).attr("action"),
      // data: "data",
      dataType: "json",
      success: function (response) {
        $(".cart-div").html(response.cart_item);
        $(".cart-list-div").html(response.cart_list);
        $("#cart-removed-alert")
          .html(`<div class="alert alert-danger alert-dismissible" role="alert">
        <button type="button" class="close" data-dismiss="alert" aria-label="Close">
          <span style="font-size: larger; color:black !important" aria-hidden="true">&times;</span>
        </button>
        <strong>Item Removed from the Cart!</strong>
      </div>`);
        setTimeout(() => {
          $("#cart-removed-alert").html(``);
        }, 4000);
      },
    });
  });

  // Add to cart-list
  $(document).on("submit", "form.add-to-cart", function (event) {
    event.preventDefault();
    console.log("I am clicked!");
    console.log($(this).attr("action"));

    $.ajax({
      type: "get",
      url: $(this).attr("action"),
      dataType: "json",
      success: function (response) {
        console.log("Success in adding 2 cart");
        $(".cart-div").html(response.cart_item);
        $(".cart-list-div").html(response.cart_list);
        $(".wish-cart-status-div").html(response.product_data);
        $("#wish-cart-model").modal("show");
      },
      error: function (err) {
        console.log("ERR", err.responseText);
      },
    });
  });

  // Add to wish-list
  $(document).on("submit", "form.add-to-wish", function (event) {
    event.preventDefault();
    console.log("I am clicked!");
    console.log($(this).attr("action"));

    $.ajax({
      type: "get",
      url: $(this).attr("action"),
      dataType: "json",
      success: function (response) {
        $(".wish-div").html(response.wish_item);
        $(".wish-cart-status-div").html(response.product_data);
        $(".cart-list-div").html(response.cart_list);
        $("#wish-from-detail").html(
          '<i class="fa fa-heart fa-2x" style="color: red !important;"></i><span class="tooltipp text-capitalize" style="font-size: large;">Added to wishlist</span>'
        );
        $("#wish-cart-model").modal("show");

        console.log("Wish modal triggered");
      },
    });
  });


// Ajaxified Question Answer Section
  $(document).on("submit", "form.ques-ans-form", function (event) {
    event.preventDefault();
    console.log($(this).attr("action"));
    data = $(this).serializeArray();
    data.push({
      name: "csrfmiddlewaretoken",
      value: $('input[name="csrfmiddlewaretoken"]').val(),
    });
    console.log($(this).serializeArray());

    $.ajax({
      type: "post",
      url: $(this).attr("action"),
      data: data,
      dataType: "json",
      success: function (response) {
        $(".ques-ans-div").html(response.ques_ans_data);
        console.log("Question or Ans asked or answered!");
        console.log(response.ques_ans_data);
        $("#question-count").html(
          `Customer Questions and Seller Answers(${response.question_count})`
        );
      },
      error: (err) => {
        console.log("Err occured...");

        console.log(err.responseText);
      },
    });
  });

//   Ajaxified Review Section
  $(document).on("submit", "form.review-form", function (event) {
    event.preventDefault();
    data = $(this).serializeArray();
    data.push({
      name: "csrfmiddlewaretoken",
      value: $('input[name="csrfmiddlewaretoken"]').val(),
    });
    console.log($(this).serializeArray());

    $.ajax({
      type: "post",
      url: $(this).attr("action"),
      data: data,
      dataType: "json",
      success: function (response) {
        $(".review-div").html(response.review_data);

        $("#review-count").html(`Reviews (${parseInt(response.review_count)})`);
        console.log("rev-count:", response.review_count);
        console.log();
      },
      error: (err) => {
        console.log("Err occured...");

        console.log(err.responseText);
      },
    });
  });
});

window.onscroll = function () {
  scrollFunction();
};

// Scroll To Top Func
function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    $("#scroll2top").css("display", "block");
  } else {
    $("#scroll2top").css("display", "none");
  }
}

// When the user clicks on the button, scroll to the top of the document
function scroll2top() {
  document.body.scrollTop = 0; // For Safari
  document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}

// csrf token generator
function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    var cookies = document.cookie.split(";");
    for (var i = 0; i < cookies.length; i++) {
      var cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

// Toggle-Appreance Mode(Dark-Light) Function

function toggle_mode() {
  $.ajax({
    type: "get",
    url: "http://127.0.0.1:8000/accounts/toggle-mode/",
    success: function (response) {
      dark_mode = response.status;
      if (dark_mode) {
        $("#toggle-mode").attr(
          "href",
          "http://127.0.0.1:8000/static/css/dark-mode.css"
        );
        $("#mode-toggler").html(
          '<i class="fa fa-2x fa-globe" aria-hidden="true"></i><span style="font-size: large;"> Enable Light Mode</span>'
        );
        console.log("Dark mode enabled...");
      }
      if (!dark_mode) {
        $("#toggle-mode").attr(
          "href",
          "http://127.0.0.1:8000/static/css/light-mode.css"
        );
        $("#mode-toggler").html(
          '<i class="fa fa-2x fa-globe" aria-hidden="true"></i><span style="font-size: large;"> Enable Dark Mode</span>'
        );
        console.log("Light mode enabled...");
      }
    },

    errro: (err) => {
      console.log(err.responseText);
    },
  });
}
// Trigger Spinner Method
function triggerSpinner(this_, btnid, message) {
  console.log("Spinner triggered...");
  console.log("id", btnid);

  if ($(this_)[0].checkValidity()) {
    $(`#${btnid}`).html(
      `<span class="spinner-border spinner-border-sm" role="status" style="color:white !important;"></span> <span class="light" style="color:white !important;">${message}</span>`
    );
    setTimeout(() => {
      $(`#${btnid}`).html(`Login`);
    }, 4000);
  } else {
    console.log("Invalid form submission...");
  }
}
