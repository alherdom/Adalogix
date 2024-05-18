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

export async function patchRequest(data, url) {
  const options = {
    method: "PATCH",
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

// Router Functions

export const addRouteLayer = (routeData, map) => {
  const layerId = `agent-route-${1}`;
  agentPlan.value.routeLayer = layerId;
  map.value.addSource(layerId, {
    type: "geojson",
    data: routeData,
  });
  let routeLayer = {
    id: layerId,
    type: "line",
    source: layerId,
    layout: {
      "line-cap": "round",
      "line-join": "round",
    },
    paint: {
      "line-color": "#FF6C37",
      "line-width": 3,
    },
  };

  map.value.addLayer(routeLayer);

  return routeLayer;
};
