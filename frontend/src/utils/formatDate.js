export function formatDate(dateString) {
    const date = new Date(dateString);

    const day = date.getDate();
    const month = date.getMonth() + 1;
    const year = date.getFullYear();
    const hours = date.getHours();
    let minutes = date.getMinutes();

    minutes = minutes < 10 ? '0' + minutes : minutes;

    const formattedDate = `${day}-${month}-${year}, ${hours}:${minutes}`;

    return formattedDate;
}
