import { createRootRoute, Outlet, Link } from "@tanstack/react-router";
import { TanStackRouterDevtools } from "@tanstack/router-devtools";
import axios from "axios";

import {
  NavigationMenu,
  NavigationMenuItem,
  NavigationMenuList,
} from "@/components/ui/navigation-menu";

import ImportButton from "@/components/ImportButton";

export const Route = createRootRoute({
  notFoundComponent() {
    return <div>Page not found 404</div>;
  },
  component: () => {
    const handleFile = async (file: File) => {
      const formData = new FormData();
      formData.append("file", file);

      try {
        const { data, status } = await axios.post(
          "http://127.0.0.1:8000/upload",
          formData,
          {
            headers: {
              "Content-Type": "multipart/form-data",
            },
          }
        );

        if (status === 200) {
          alert(data.message);
          window.location.reload();
        }
      } catch (error) {
        if (axios.isAxiosError(error)) {
          if (error.response) {
            const errorMessage =
              error.response.data.error ||
              "An error occurred. Please try again.";
            alert(errorMessage);
          } else {
            console.error("No response received from server:", error.message);
          }
        } else if (error instanceof Error) {
          console.error("Unexpected error:", error);
          alert("Something went wrong. Please try again.");
        }
      }
    };

    return (
      <>
        <NavigationMenu className="mx-auto my-4 shadow shadow-slate-800 p-2 rounded-md sticky top-5 backdrop-blur-md">
          <NavigationMenuList className="text-xl gap-3 grow">
            <NavigationMenuItem>
              <Link
                to="/f2"
                activeProps={{
                  className: "font-bold",
                }}
                activeOptions={{ exact: true }}
              >
                F02
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
                F03
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
                F09
              </Link>
            </NavigationMenuItem>
          </NavigationMenuList>
          <ImportButton handleFile={handleFile}>Import File</ImportButton>
        </NavigationMenu>
        <Outlet />
        <TanStackRouterDevtools position="bottom-right" />
      </>
    );
  },
});
