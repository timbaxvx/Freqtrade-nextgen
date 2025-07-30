import React from "react";
import Link from "next/link";

interface NavLinkProps {
  href: string;
  children: React.ReactNode;
}

const NavLink: React.FC<NavLinkProps> = ({ href, children }) => (
  <Link href={href} className="text-neon-cyan hover:text-neon-lime transition duration-300 ease-in-out">
    {children}
  </Link>
);

export default function Navbar() {
  // In a real application, you would fetch the user's role from context or a global state
  const userRole = "admin"; // Placeholder: "beginner", "advanced", "expert", "admin", "developer"

  const navItems = [
    { name: "Dashboard", href: "/" },
    { name: "Bots", href: "/bots" },
    { name: "Strategies", href: "/strategies" },
    { name: "Analytics", href: "/analytics" },
    { name: "Integrations", href: "/integrations" },
    { name: "Settings", href: "/settings" },
    { name: "Assistant", href: "/assistant" },
    { name: "Onboarding", href: "/onboarding" },
  ];

  return (
    <nav className="bg-glass p-4 shadow-neon-cyan backdrop-blur-xs sticky top-0 z-50">
      <div className="container mx-auto flex justify-between items-center">
        <div className="text-2xl font-bold text-neon-cyan drop-shadow-neon-cyan">
          <Link href="/">Freqtrade NextGen</Link>
        </div>
        <ul className="flex space-x-6">
          {navItems.map((item) => (
            <li key={item.name}>
              <NavLink href={item.href}>{item.name}</NavLink>
            </li>
          ))}
        </ul>
        import NotificationList from './NotificationList';

// ... (rest of the file)

        {/* User/Auth section - placeholder */}
        <div className="flex items-center gap-4">
          <NotificationList />
          <img src="/avatar.png" alt="User" className="w-8 h-8 rounded-full border-2 border-neon-cyan" />
        </div>
      </div>
    </nav>
  );
}