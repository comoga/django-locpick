//#google.load("maps", "2");

/*$(document).unload(function(){
    GUnload();
});
*/

$(document).ready(function(){
    $("input.location_picker").each(function (i) {
        var map = $('<div>');
        var input = this;
        map.addClass("location_picker_map");
        map.attr('id', 'location_picker_map');
        $(this).parent().append(map);
        $(this).css('display','none');

        if (this.value.split(',').length == 5) {
            values = this.value.split(',');
            var position = new google.maps.LatLng(values[0], values[1]);
            var center = new google.maps.LatLng(values[2], values[3]);
            var zoom = parseInt(values[4]);
        } else {
            var center = new google.maps.LatLng(50.1, 14.4);
            var position = null;
            var zoom = 12;
        }


        var myOptions = {
          zoom: zoom,
          center: center,
          mapTypeControl: false,
          streetViewControl: false,
          mapTypeId: google.maps.MapTypeId.ROADMAP
        };
        var gmap = new google.maps.Map(document.getElementById("location_picker_map"), myOptions);

        if (position != null) {
            var marker = new google.maps.Marker({
                position: position,
                map: gmap,
            });
        } else {
            var marker = null;
        }

        function update_input(){
            var pos = marker.getPosition();
            input.value = pos.lat()
                        + ',' + pos.lng()
                        + ',' + gmap.getCenter().lat()
                        + ',' + gmap.getCenter().lng()
                        + ',' + gmap.getZoom();
        }
        google.maps.event.addListener(gmap, 'click', function(event) {
            if (marker == null) {
                marker = new google.maps.Marker({
                    position: event.latLng,
                    map: gmap,
                });
            } else {
                marker.setPosition(event.latLng);
            }
            update_input();
        });

        google.maps.event.addListener(gmap, 'center_changed', function(event) {
            update_input();
        });
        google.maps.event.addListener(gmap, 'zoom_changed', function(event) {
            update_input();
        });

        function HomeControl(controlDiv, gmap) {

          controlDiv.style.padding = '5px';

          // Set CSS for the control border
          var controlUI = document.createElement('DIV');
          controlUI.style.backgroundColor = 'white';
          controlUI.style.borderStyle = 'solid';
          controlUI.style.borderWidth = '2px';
          controlUI.style.cursor = 'pointer';
          controlUI.style.textAlign = 'center';
          controlUI.title = 'Click to remove the marker';
          controlDiv.appendChild(controlUI);

          // Set CSS for the control interior
          var controlText = document.createElement('DIV');
          controlText.style.fontFamily = 'sans-serif';
          controlText.style.fontSize = '12px';
          controlText.style.paddingLeft = '4px';
          controlText.style.paddingRight = '4px';
          controlText.innerHTML = 'Clean';
          controlUI.appendChild(controlText);

          // Setup the click event listeners: simply set the map to Chicago
          google.maps.event.addDomListener(controlUI, 'click', function() {
            if (marker != null){
              marker.setMap(null);
              marker = null;
              input.value = '';
            }
          });
        }
        var homeControlDiv = document.createElement('DIV');
        var homeControl = new HomeControl(homeControlDiv, gmap);

        homeControlDiv.index = 1;
        gmap.controls[google.maps.ControlPosition.TOP_RIGHT].push(homeControlDiv);
    });
});
