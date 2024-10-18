import { createRootRoute, Outlet, Link } from "@tanstack/react-router";
import { TanStackRouterDevtools } from "@tanstack/router-devtools";

import {
  NavigationMenu,
  NavigationMenuItem,
  NavigationMenuLink,
  NavigationMenuList,
} from "@/components/ui/navigation-menu";

import ImportButton from "@/components/ImportButton";

export const Route = createRootRoute({
  component: RootComponent,
});

function RootComponent() {
  return (
    <>
      <NavigationMenu className="mx-auto my-4 shadow shadow-slate-800 p-2 rounded-md">
        <NavigationMenuList className="text-xl gap-3 grow">
          <NavigationMenuItem>
            <Link
              to="/f2"
              activeProps={{
                className: "font-bold",
              }}
              activeOptions={{ exact: true }}
            >
              <NavigationMenuLink>F02</NavigationMenuLink>
            </Link>
          </NavigationMenuItem>
          <NavigationMenuItem>
            <Link
              to="/f3"
              activeProps={{
                className: "font-bold",
              }}
              activeOptions={{ exact: true }}
            >
              <NavigationMenuLink>F03</NavigationMenuLink>
            </Link>
          </NavigationMenuItem>
          <NavigationMenuItem>
            <Link
              to="/f9"
              activeProps={{
                className: "font-bold",
              }}
              activeOptions={{ exact: true }}
            >
              <NavigationMenuLink>F09</NavigationMenuLink>
            </Link>
          </NavigationMenuItem>
        </NavigationMenuList>
        <ImportButton>Import File</ImportButton>
      </NavigationMenu>
      <Outlet />
      <TanStackRouterDevtools position="bottom-right" />
    </>
  );
}
