import { ReactNode } from "react"

type PageCardProps = {
    image?: string,
    children: ReactNode,
    imageWidth?: string
}

export default function PageCard({ image, children, imageWidth }: PageCardProps) {
    return (
        <div className="w-full aspect-square bg-cmidgrey flex flex-col justify-between items-start select-none cursor-pointer">
            <div className="self-start font-grtskmegabold text-sm ml-12 mt-6">{children}</div>
            {image ? <img className={`self-end mb-6 mr-12 ${imageWidth ?? 'w-20'}`} src={image} /> : null}
        </div>
    )
}