import "./globals.css";

export const metadata = {
  title: "RankPilot AI",
  description: "AI SEO Traffic Platform",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>
        {children}
      </body>
    </html>
  );
}
