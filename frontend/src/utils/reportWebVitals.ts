// import { type ReportCallback } from 'web-vitals';
import { type MetricType } from 'web-vitals';

export interface ReportCallbackMy {
    (metric: MetricType): void;
}
// interface ReportCallback
// (metric: MetricType) => void

const reportWebVitals = (onPerfEntry?: ReportCallbackMy) => {
    if (onPerfEntry && onPerfEntry instanceof Function) {
        import('web-vitals').then(({ onCLS, onINP, onFCP, onLCP, onTTFB }) => {
            onCLS(onPerfEntry);
            onINP(onPerfEntry);
            onFCP(onPerfEntry);
            onLCP(onPerfEntry);
            onTTFB(onPerfEntry);
        });
    }
};

export default reportWebVitals;
