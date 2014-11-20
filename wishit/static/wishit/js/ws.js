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
		var gift_id = $(".gift_id").val();
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
								$(".modal-body .gift_title").empty();
								$(".modal-body .gift_id").val('');
								$('#myModal').modal('hide');
					},
					error : function(xhr,errmsg,err) {
									alert(xhr.status + ": " + xhr.responseText);
					}
			});
			return false;
	});
	$("#save_changes_btn").click(function() {
		var gift_id = $(".gift_id").val();
		var title = $("#edit_title_inp").val();
		var text = $("#edit_text_inp").val();
			$.ajax({
					url : "/wishit/update_gift", 
					type : "POST",
					dataType: "text", 
					data : {
						gift_id : gift_id,
						title : title,
						text : text,
							csrfmiddlewaretoken: csrftoken
							},
							success : function(data) {
								$('#wl').html(data);
								$(".modal-body .gift_title").empty();
								$(".modal-body .gift_id").val('');
								$("#edit_item_form #edit_title_inp").val('');
								$("#edit_item_form #edit_text_inp").val('');
								$('#my_edit_modal').modal('hide');
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
		$(document).on("click", ".del_edit_btn", function () {
				 var myTitle = $(this).data('title');
				 var myId = $(this).data('id');
				 var myText = $(this).data('text');
				 $(".modal-body .gift_title").append( myTitle );
				 $(".modal-body .gift_id").val( myId );
				 $("#edit_item_form #edit_title_inp").val( myTitle );
				 $("#edit_item_form #edit_text_inp").val( myText );
		});
		$(document).on("click", ".md_cancel, .close_md", function () {
				 $(".modal-body .gift_title").empty();
				 $(".modal-body .gift_id").val('');
				 $("#edit_item_form #edit_title_inp").val('');
				 $("#edit_item_form #edit_text_inp").val('');
		});

});

$(document).ready(function(){
    $('.login_form').bootstrapValidator({
        container: '.messages',
        feedbackIcons: {
            valid: 'glyphicon glyphicon-ok',
            invalid: 'glyphicon glyphicon-remove',
            validating: 'glyphicon glyphicon-refresh'
				},
				fields: {
					username : {
						validators: {
								notEmpty: {
									message: 'The username is required to be filled out'
								}
						}
					},
					password: {
						validators: {
								notEmpty: {
									message: 'The password is required to be filled out'
								}
						}
					},
					password1: {
						validators: {
								notEmpty: {
									message: 'The password is required to be filled out'
								},
								identical: {
									field: 'password2',
									message: 'The password and its confirm are not the same'
								}
						}
					},
					password2: {
						validators: {
								notEmpty: {
									message: 'The password is required to be filled out'
								},
								identical: {
									field: 'password1',
									message: 'The password and its confirm are not the same'
								}
						}
					}

				}
			});
});


