"use client";
import Link from "next/link";
import { usePathname } from "next/navigation";
import { Shield, TrendingDown, Zap, LayoutDashboard, DollarSign, FileText, Users, Rocket, Instagram } from "lucide-react";

const shieldNav = [
    { href: "/dashboard", label: "Overview", icon: LayoutDashboard },
    { href: "/dashboard/reach", label: "Reach Health", icon: TrendingDown },
    { href: "/dashboard/shield", label: "Comment Shield", icon: Shield },
    { href: "/dashboard/workload", label: "Workload Signals", icon: Zap },
    { href: "/dashboard/instagram", label: "Instagram Reels", icon: Instagram },
];

const acceleratorNav = [
    { href: "/dashboard/accelerator", label: "Overview", icon: Rocket },
    { href: "/dashboard/accelerator/pricing", label: "Brand Deal Pricing", icon: DollarSign },
    { href: "/dashboard/accelerator/scripts", label: "Script Generator", icon: FileText },
    { href: "/dashboard/accelerator/matching", label: "Brand Matching", icon: Users },
];

function NavLink({ href, label, icon: Icon, pathname }: { href: string; label: string; icon: React.ElementType; pathname: string }) {
    const active = pathname === href;
    return (
        <Link href={href} className={`flex items-center gap-3 px-3 py-2 rounded-lg text-sm font-medium transition-all ${active ? "bg-indigo-500/20 text-indigo-300" : "text-gray-400 hover:text-white hover:bg-white/[0.05]"
            }`}>
            <Icon size={15} />
            {label}
        </Link>
    );
}

export default function DashboardLayout({ children }: { children: React.ReactNode }) {
    const pathname = usePathname();

    return (
        <div className="flex min-h-screen">
            {/* Sidebar */}
            <aside className="w-60 flex-shrink-0 border-r border-white/[0.06] flex flex-col"
                style={{ background: "var(--surface-2)" }}>

                {/* Logo */}
                <div className="flex items-center gap-3 px-5 py-4 border-b border-white/[0.06]">
                    <div className="w-8 h-8 rounded-lg bg-indigo-500 flex items-center justify-center">
                        <Shield size={15} className="text-white" />
                    </div>
                    <div>
                        <span className="font-bold text-sm text-white tracking-wide">Inflomnia</span>
                        <p className="text-[10px] text-indigo-400 font-medium">Phase 1</p>
                    </div>
                </div>

                <nav className="p-3 flex-1 space-y-4 overflow-y-auto">
                    {/* The Shield */}
                    <div>
                        <p className="px-3 text-[10px] font-semibold uppercase tracking-widest text-gray-600 mb-1">
                            🛡️ The Shield
                        </p>
                        <div className="space-y-0.5">
                            {shieldNav.map(item => (
                                <NavLink key={item.href} {...item} pathname={pathname} />
                            ))}
                        </div>
                    </div>

                    {/* The Accelerator */}
                    <div>
                        <p className="px-3 text-[10px] font-semibold uppercase tracking-widest text-gray-600 mb-1">
                            🚀 The Accelerator
                        </p>
                        <div className="space-y-0.5">
                            {acceleratorNav.map(item => (
                                <NavLink key={item.href} {...item} pathname={pathname} />
                            ))}
                        </div>
                    </div>
                </nav>

                {/* Footer */}
                <div className="p-3 border-t border-white/[0.06]">
                    <div className="rounded-lg p-3 text-[11px] text-gray-500"
                        style={{ background: "var(--surface-3)", border: "1px solid var(--border)" }}>
                        <p className="font-semibold text-gray-400 mb-0.5">📡 Status</p>
                        <span className="text-green-400">● API Connected</span>
                    </div>
                </div>
            </aside>

            {/* Main content */}
            <main className="flex-1 overflow-auto">
                {children}
            </main>
        </div>
    );
}
