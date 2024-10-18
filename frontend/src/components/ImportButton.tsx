import React from "react";
import { Button } from "./ui/button";

import { DownloadIcon } from "@radix-ui/react-icons";

type Props = {
  children: React.ReactNode;
};

const ImportButton = (props: Props) => {
  return (
    <Button className="ml-32 font-bold bg-blue-600 hover:bg-blue-700">
      {props.children}
      <DownloadIcon />
    </Button>
  );
};

export default ImportButton;
