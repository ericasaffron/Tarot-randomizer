export default function handler(req, res) {
  const n = Math.floor(Math.random() * 22);
  res.setHeader("Cache-Control", "no-store, max-age=0, must-revalidate");
  res.redirect(302, `/composed/${n}.png`);
}
