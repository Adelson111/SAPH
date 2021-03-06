/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package rest;

import banco.Persistencia;
import modelo.Comentario;

import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;
import java.util.List;
import javax.ws.rs.Consumes;
import javax.ws.rs.DELETE;
import javax.ws.rs.GET;
import javax.ws.rs.POST;
import javax.ws.rs.PUT;
import javax.ws.rs.Path;
import javax.ws.rs.PathParam;
import javax.ws.rs.Produces;
import javax.ws.rs.core.MediaType;

/**
 *
 * @author adelson
 */
@Path("solicitacao-delegacao")
public class SolicitacaoDelegacao {

    @POST
    @Consumes(MediaType.APPLICATION_JSON)
    public String cadastrar(String json) {
    	modelo.SolicitacaoDelegacao solicitacao = new Gson().fromJson(json, modelo.SolicitacaoDelegacao.class);
    	Persistencia persistencia = new Persistencia();
    	for(modelo.Item item:solicitacao.getItens()) {
    		for(modelo.Campo campo:item.getCampos()) {
    			persistencia.cadastrar(campo);
    		}
    		persistencia.cadastrar(item);
    	}
        return persistencia.cadastrar(solicitacao);
    }

    @POST
    @Consumes(MediaType.APPLICATION_JSON)
    @Path("lista")
    public String cadastrarLista(String json) {
        return new Persistencia().cadastrar((List<Object>) new Gson().fromJson(json, new TypeToken<List<modelo.SolicitacaoDelegacao>>() {
        }.getType()));
    }
    
    
    @POST
    @Consumes(MediaType.APPLICATION_JSON)
    @Path("alterar-status")
    public String enviar(String solicitacaoDelegacao) {
    	modelo.SolicitacaoDelegacao sd = new Gson().fromJson(solicitacaoDelegacao, modelo.SolicitacaoDelegacao.class);
    	Persistencia persistencia = new Persistencia();
        if(!sd.equals(persistencia.selecionar(sd, sd.getId()))) {
        	return cadastrar(solicitacaoDelegacao);
        }else {
        	return persistencia.atualizar(sd);
        }
    }
    
    
    @POST
    @Consumes(MediaType.APPLICATION_JSON)
    @Path("comentar")
    public String comentar(String comentario) {
    	System.out.println(comentario);
    	new Persistencia().cadastrar(new Gson().fromJson(comentario, Comentario.class));
    	return comentario;
    }


    @PUT
    @Consumes(MediaType.APPLICATION_JSON)
    public String atualizar(String json) {
        return new Persistencia().atualizar(new Gson().fromJson(json, modelo.SolicitacaoDelegacao.class));
    }
    
    @POST
    @Consumes(MediaType.APPLICATION_JSON)
    @Path("atualizar")
    public String atualizarSD(String json) {
    	Persistencia persistencia = new Persistencia();
    	modelo.SolicitacaoDelegacao solicitacaoDelegacao = new Gson().fromJson(json, modelo.SolicitacaoDelegacao.class);
    	for(modelo.Item item:solicitacaoDelegacao.getItens()) {
    		for(modelo.Campo campo:item.getCampos()) {
    			persistencia.atualizar(campo);
    		}
    	}
        return "Ataualizado com sucesso";
    }

    @DELETE
    @Consumes(MediaType.TEXT_PLAIN)
    @Path("{id}")
    public String remover(@PathParam("id") long id) {
        return new Persistencia().remover(new modelo.SolicitacaoDelegacao(), id);
    }

    @GET
    @Produces(MediaType.APPLICATION_JSON)
    public String selecionar() {
        return new Gson().toJson(new Persistencia().selecionar(new modelo.SolicitacaoDelegacao()));
    }
    @GET
    @Produces(MediaType.APPLICATION_JSON)
    @Path("recebidas/{funcionario}/{solicitaca}")
    public String recebidas(@PathParam("funcionario") String funcionario, @PathParam("solicitaca") boolean solicitaca) {
        return new Gson().toJson(new Persistencia().recebidas(Long.parseLong(funcionario),solicitaca));
    }
    @GET
    @Produces(MediaType.APPLICATION_JSON)
    @Path("{id}")
    public String selecionar(@PathParam("id") long id) {
        return new Gson().toJson(new Persistencia().selecionar(new modelo.SolicitacaoDelegacao(), id));
    }
    @GET
    @Produces(MediaType.APPLICATION_JSON)
    @Path("parametros/{tipo}/{solicitanteDelegante}")
    public String selecionar(@PathParam("tipo") tipo.TipoSolicitacaoDelegacao tipo,@PathParam("solicitanteDelegante") long solicitanteDelegante) {
        return new Gson().toJson(new Persistencia().getSolicitacaoDelegacao(tipo,solicitanteDelegante));
    }
    
    @GET
    @Produces(MediaType.APPLICATION_JSON)
    @Path("comentarios/{solicitacao}")
    public String comentarios(@PathParam("solicitacao") String solicitacaoDelegacao) {
    	System.out.println(solicitacaoDelegacao);
    	modelo.SolicitacaoDelegacao sd = new Gson().fromJson(solicitacaoDelegacao, modelo.SolicitacaoDelegacao.class);
        return new Gson().toJson(new Persistencia().comentarios(sd));
    }
    
    

}
