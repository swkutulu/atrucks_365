// type UseQueryResult<T>
interface QueryResult {
  // Arguments passed to the query
  originalArgs?: [];
  
  data?: object[];
  currentData?: object[];
  error?: unknown;
  requestId?: string;
  endpointName?: string;
  startedTimeStamp?: number;
  fulfilledTimeStamp?: number;

  isUninitialized: boolean;
  isLoading: boolean;
  isFetching: boolean;
  isSuccess: boolean;
  isError: boolean;

//   refetch: () => ()
//   refetch: () => QueryActionCreatorResult
};


// import { Use } from '@reduxjs/toolkit/query/react';

export class ResultsHandler {
    private errors: string[] = [];
    
    private isLoading: boolean[] = [];
    private isError: boolean[] = [];
    private isFetching: boolean[] = [];
    private isSuccess: boolean[] = [];

    constructor() {
        // this.errors = [];
        // super(message);
    }
    
    // handleResults(res: QueryResult): QueryResult {
    handleResults(res) {
        this.isLoading.push(res.isLoading);
        this.isLoading.push(res.isLoading);
        this.isError.push(res.isError);
        this.isFetching.push(res.isFetching);
        this.isSuccess.push(res.isSuccess);

        if(Object.prototype.hasOwnProperty.call(res, "error") && res.error) {
            if(res.error.data?.detail && this.errors.indexOf(res.error.data?.detail) === -1)
                this.errors.push(res.error.data.detail);
        }
        return res;
    };

    getIsBusy(): boolean {
        return this.getIsLoading() || this.getIsFetching();
    }

    getIsLoading(): boolean {
        return this.isLoading.some((element) => {
            if(element) {
                return true;
            }
        })
    }

    getIsError(): boolean {
        return this.isError.some((element) => {
            if(element) {
                return true;
            }
        })
    }

    getIsFetching(): boolean {
        return this.isFetching.some((element) => {
            if(element) {
                return true;
            }
        })
    }

    getIsSuccess(): boolean {
        return this.isSuccess.some((element) => {
            if(element) {
                return true;
            }
        })
    }

    getErrors(): string[] {
        return this.errors;
    }
}