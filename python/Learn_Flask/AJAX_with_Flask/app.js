const callAJAX = (props) => {
    const url = props.url,
        method = props.method || "GET",
        type = props.type || "JSON",
        header = props.header
    ;
    
    return new Promise(waitForResponse => {
        const xhttp = new XMLHttpRequest();
        if (method === "GET") {
            xhttp.open("GET", url, true);
            for (const key in header) {
                xhttp.setRequestHeader(key, header[key]);
            }
            xhttp.send();
        } else {
            xhttp.open("POST", url, true);
            for (const key in header) {
                xhttp.setRequestHeader(key, header[key]);
            }
            xhttp.send(props.data);
        }
        xhttp.onreadystatechange = function() {
            if (this.readyState === 4 && this.status === 200) {
                console.log(this.response);
                type === "text"
                    ? waitForResponse(this.response)
                    : waitForResponse(JSON.parse(this.response))
                ;
            }
        };
    });
};

const sendMessage = () => {
    const message = document.getElementById("message").value;
    const data = {
        message: message
    };
    
    const AJAXProps = {
        url: "http://localhost:5000/api/",
        header: {
            "Content-type": "application/json"
        },
        method: "POST",
        data: `${JSON.stringify(data)}`
    };
    
    callAJAX(AJAXProps).then(response => {
        console.log("response", response);
    });
}

document.getElementById("send").addEventListener("click", sendMessage);