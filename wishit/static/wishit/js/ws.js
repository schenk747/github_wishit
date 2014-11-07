function toggle_glyph() 
{
	$("#glyph_add_item").toggleClass("glyphicon glyphicon-plus glyphicon glyphicon-minus");
}


$(document).ready(function() {
	$("#add_item").click(function() {
		var title = $("#title").val();
		var text = $("#text").val();
		var wl_id = $("#wl_id").val();
			$.ajax({
					url : "/wishit/update_wishlist", 
					type : "POST",
					dataType: "text", 
					data : {
							title: title,
							text : text,
							wl_id : wl_id,
							csrfmiddlewaretoken: csrftoken
							},
					success : function(data) {
							$('#wl').html(data);
							$( '#add_item_form' ).each(function(){
   							 this.reset();
							});
					},
					error : function(xhr,errmsg,err) {
									alert(xhr.status + ": " + xhr.responseText);
					}
			});
			return false;
	});

	$("#del_gift_confirm").click(function() {
		var gift_id = $("#gift_id").val();
			$.ajax({
					url : "/wishit/delete_gift", 
					type : "POST",
					dataType: "text", 
					data : {
						gift_id : gift_id,
							csrfmiddlewaretoken: csrftoken
							},
							success : function(data) {
								$('#wl').html(data);
								$(".modal-body #gift_title").empty();
								$(".modal-body #gift_id").val('');
								$('#myModal').modal('hide');
					},
					error : function(xhr,errmsg,err) {
									alert(xhr.status + ": " + xhr.responseText);
					}
			});
			return false;
	});

});

$(document).ready(function () {
    $(document).on('mouseenter', '.btn-align', function () {
        $(this).find(".gift-button").removeClass("not-visible");
    }).on('mouseleave', '.btn-align', function () {
        $(this).find(".gift-button").addClass("not-visible");
    });
		$(document).on("click", ".del_btn", function () {
				 var myTitle = $(this).data('title');
				 var myId = $(this).data('id');
				 $(".modal-body #gift_title").append( myTitle );
				 $(".modal-body #gift_id").val( myId );

		});
		$(document).on("click", "#del_cancel, #close_del_gift", function () {
				 $(".modal-body #gift_title").empty();
				 $(".modal-body #gift_id").val('');
		});

});

