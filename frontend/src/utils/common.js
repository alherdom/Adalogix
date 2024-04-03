import Swal from "sweetalert2";

export async function postLoginRequest(data, url) {
  const options = {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  };

  const response = await fetch(url, options);
  return await response.json();
}

export async function postRequest(data, url) {
  const options = {
    method: "POST",
    headers: {
      Authorization: `Token ${localStorage.getItem("userToken")}`,
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  };

  const response = await fetch(url, options);
  return await response.json();
}

export async function getRequest(url) {
  const options = {
    method: "GET",
    headers: {
      Authorization: `Token ${localStorage.getItem("userToken")}`,
      "Content-Type": "application/json",
    },
  };

  const response = await fetch(url, options);
  return await response.json();
}

export async function deleteRequest(data, url) {
  const options = {
    method: "DELETE",
    headers: {
      Authorization: `Token ${localStorage.getItem("userToken")}`,
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  };

  const response = await fetch(url, options);
  return await response.json();
}

export const logout = () => {
  sessionStorage.clear();
  this.$router.push("/login");
  Swal.fire({
    title: "Success",
    text: "Logged out successfully",
    icon: "success",
    showConfirmButton: false,
    timer: 1500,
  });
};
