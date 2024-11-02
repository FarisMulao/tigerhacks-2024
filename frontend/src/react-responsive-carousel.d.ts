declare module 'react-responsive-carousel' {
  import React from 'react';
  
  export interface CarouselProps {
    showArrows?: boolean;
    autoPlay?: boolean;
    infiniteLoop?: boolean;
    interval?: number;
    showThumbs?: boolean;
    showStatus?: boolean;
    dynamicHeight?: boolean;
    children?: React.ReactNode;
  }
  
  export class Carousel extends React.Component<CarouselProps> {}
}
