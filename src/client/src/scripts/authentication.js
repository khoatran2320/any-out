//cookie functions obtained from https://plainjs.com/javascript/utilities/set-cookie-get-cookie-and-delete-cookie-5/
export function getCookie(name) {
  var v = document.cookie.match("(^|;) ?" + name + "=([^;]*)(;|$)");
  return v ? v[2] : null;
}

export function addCookie(name, value) {
  document.cookie = name + "=" + value + "; Path=/;";
}
export function deleteCookie(name) {
  document.cookie = name + "=; Path=/; Expires=Thu, 01 Jan 1970 00:00:01 GMT;";
}

export function wasAlreadyLoggedIn() {
  if (getCookie("SID")) {
    return true;
  } else {
    return false;
  }
}
