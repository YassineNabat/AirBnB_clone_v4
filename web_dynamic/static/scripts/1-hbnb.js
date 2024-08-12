
$(document).ready(function() {
	//Initialize an empty object to hold selected amenities
	var selectedAmenities = {};
	
	//Listen for changes on checkboxes
	$('.amenity-checkbox').change(function() {
		const amenityId = $(this).data('id');
		const amenityName = $(this).data('name');
	//
		if ($(this).is(':checked')) {
			selectedAmenities[amenityId] = amenityName;
		} else {
			delete selectedAmenities[amenityId];
		}
	
		updateDisplay();
	});
	function updateDisplay() {
		const amenitiesDiv = $('#amenities');
		const amenitiesList = Object.entries(selectedAmenities).map(([id, name]) => `${name} (${id})`).join(', ');
		amenitiesDiv.find('h4').text(`Selected Amenities: ${amenitiesList}`);
	}
});
