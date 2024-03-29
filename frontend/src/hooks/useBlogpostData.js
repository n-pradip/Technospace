import { useQuery } from "react-query";
import {api} from "../api/rootApi";


const getBlogpost=(id)=> api.get(`blog/posts/${id}`).then((res) => res.data);

const useBlogpostData = (id) =>{
    return useQuery(['blogpost',id], ()=>getBlogpost(id))
}

export default useBlogpostData;