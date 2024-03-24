export async function postRequest(data, url) {
  const options = {
    method: 'POST',
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  };

  const response = await fetch(url, options);
  return await response.json();
}

export async function getRequest(url) {
  const options = {
    method: 'GET',
    headers: {
      "Content-Type": "application/json",
    },
  };

  const response = await fetch(url, options);
  return await response.json();
}
