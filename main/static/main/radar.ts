let map: google.maps.Map;
function initMap(): void {
    map = new google.maps.Map(document.getElementById("map") as HTMLElement, {
        center: {lat: 37.486, lng: 139.927},
        zoom: 13
    });
    const url = new URL("./getUser", location.href);
    const request = new Request(url.toString());
    fetch(request).then(async (response) => {
        if (response.ok) {
            const data = await response.json()
            data.forEach((user) => {
                const size = new google.maps.Size(40, 40);
                const symbol: google.maps.Icon = {
                    url: "/static/main/women.png",
                    scaledSize: size
                }
                const marker = new google.maps.Marker({
                    position: {
                        lat: user.fields["Latitude"],
                        lng: user.fields["Longitude"]
                    },
                    map: map,
                    title: user.fields["Name"],
                    icon: symbol
                });
                const content =
                    "<h1>" + user.fields["Name"] + "</h1>" +
                    `<p style="font-size:${user.fields['Size']}px;">${user.fields['Status']}</p>`
                const infowindow = new google.maps.InfoWindow({
                    content: content
                });
                marker.addListener('click', function () {
                    infowindow.open(map, marker);
                });

            })
        }
    });
}
