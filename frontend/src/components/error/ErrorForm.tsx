import React from "react";

export const ErrorForm = ({error, field_name}: {error: ApiError | undefined, field_name: string}) => {
    const result: React.ReactNode[] = []
    const uniq: string[] = [];
    if(error){
        if(Object.prototype.hasOwnProperty.call(error, 'data') 
            && Object.prototype.hasOwnProperty.call(error.data, field_name)
    ){
            try{
                error.data[field_name].forEach((element: unknown) => {
                    if(typeof(element) === 'string'){
                        uniq.push(element);
                    }
                    if(typeof(element) === 'object'){
                        Object.entries(element as object).forEach(([key, value]) => {
                            uniq.push(value);
                        });
                    }
                });
            } catch(e) {
                console.log(e);
            }
        }   
    }
    let key = 1;
    [...new Set(uniq)].forEach((el: string) => {
        result.push(
            <p key={key++} className="absolute text-xs text-(--color-error)">{el}</p>
        )
    })
    return (result)
}
