export const baseUrlApi = (url: string) =>
  process.env.NODE_ENV === "development"
    ? `http://192.144.133.50:3000/${url}`
    : `http://192.144.133.50:3000/${url}`;

export const baseUrlApiParam = (url: string, param) =>
  process.env.NODE_ENV === "development"
    ? `http://192.144.133.50:3000/${url}/${param}`
    : `http://192.144.133.50:3000/${url}/${param}`;
