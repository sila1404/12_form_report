import React, { useRef } from "react";
import { Button } from "./ui/button";

import { DownloadIcon } from "@radix-ui/react-icons";

type Props = {
  children: React.ReactNode;
  handleFile: (file: File) => void;
};

const ImportButton = (props: Props) => {
  const hiddenFileInput = useRef<HTMLInputElement | null>(null);

  const handleClick = () => {
    hiddenFileInput.current?.click();
  };

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const fileImported = e.target.files?.[0];
    if (fileImported) {
      props.handleFile(fileImported);
    }
  };
  return (
    <>
      <Button
        className="ml-32 font-bold bg-blue-600 hover:bg-blue-700"
        onClick={handleClick}
      >
        {props.children}
        <DownloadIcon />
      </Button>
      <input
        type="file"
        className="hidden"
        onChange={handleChange}
        ref={hiddenFileInput}
      />
    </>
  );
};

export default ImportButton;
