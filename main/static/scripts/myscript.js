
function add_material_line() {
	
	var list_length = document.getElementById("material_line_item_list").childElementCount;
	// alert("Add material line clicked : length of items : " + list_length);
	
	// Get the material line item element div
	var itm = document.getElementById("material_line_item");

	// Copy the element and its child nodes
	var cln = itm.cloneNode(true);
	cln.getElementsByClassName("quantity")[0].value = 0;
	cln.id = "material_line_item_" + list_length;
	
	// We need to change attributes of different material descriptions as following (so that all materials can be properly passed on.):
	// 1. mas_entry_material - will become mas_entry_material_2, 3 etc
	// 2. quantity - will become quantity_2, 3 etc
	// 3. unit - will become unit_2, 3 etc
	var counter = list_length + 1;
	cln.getElementsByClassName("mas_entry_material")[0].setAttribute("name", "mas_entry_material_" + counter);
	cln.getElementsByClassName("quantity")[0].setAttribute("name", "quantity_" + counter);
	cln.getElementsByClassName("unit")[0].setAttribute("name", "unit_" + counter);
	
	// cln.getElementsByClassName("delete_material_line")[0].setAttribute("disabled", "false")
	cln.getElementsByClassName("delete_material_line")[0].disabled = false

	// Append the cloned element to material_line_item_list
	document.getElementById("material_line_item_list").appendChild(cln);
		
	// Increase no of materials counter in no_of_materials element.
	var list_length = document.getElementById("material_line_item_list").childElementCount;
	document.getElementById("no_of_materials").setAttribute("value", list_length);
	
	// Scrolling to newly added item.
	window.scroll(0,findPos(document.getElementById(cln.id)));
}

function delete_material_line(svar) {
	// alert("Delete material line clicked. : " + svar.parentNode.id);
	
	// var elt = svar;
	// // Traverse up until root hit or DIV with ID found
	// while (elt && (elt.tagName != "div" || !elt.id))
            // elt = elt.parentNode;
        // if (elt) // Check we found a DIV with an ID
            // alert(elt.id);
	
	document.getElementById(svar.parentNode.id).remove();
	
	// Decrease no of materials counter in no_of_materials element.
	var list_length = document.getElementById("material_line_item_list").childElementCount;
	document.getElementById("no_of_materials").setAttribute("value", list_length);
}

// Reference from https://stackoverflow.com/questions/5007530/how-do-i-scroll-to-an-element-using-javascript
//Finds y value of given object
function findPos(obj) {
    var curtop = 0;
    if (obj.offsetParent) {
        do {
            curtop += obj.offsetTop;
        } while (obj = obj.offsetParent);
    return [curtop];
    }
}
