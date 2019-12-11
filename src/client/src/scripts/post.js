import axios from "axios";

const apiUrl = "http://localhost:4000";

const axiosConfig = {
  headers: {
    "content-type": "application/x-www-form-urlencoded",
    "Access-Control-Allow-Origin": "*"
  }
};

function urlEncode(data) {
  var urlEncodedString = "";
  Object.keys(data).forEach(function(key) {
    urlEncodedString += key + "=" + encodeURIComponent(data[key]) + "&";
  });
  return urlEncodedString.slice(0, -1);
}

export function post(endpoint, payload) {
  return new Promise((resolve, reject) => {
    axios
      .post(apiUrl + endpoint, urlEncode(payload), axiosConfig)
      .then(response => {
        resolve(response);
      })
      .catch(error => {
        reject(error);
      });
  });
}
