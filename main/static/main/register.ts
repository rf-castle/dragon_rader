
function getPosition(){
    function success(position: Position){
        const coords = position.coords
        const form = document.forms[0]
        form.elements["latitude"].value = coords.latitude
        form.elements["longitude"].value = coords.longitude
    }
    navigator.geolocation.getCurrentPosition(success, (error => error), {})
}

