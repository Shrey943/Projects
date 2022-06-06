package com.example.credence.adapter;

import android.annotation.SuppressLint;
import android.content.Context;
import android.content.Intent;
import android.util.AttributeSet;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import com.example.credence.EditActivity;

import com.example.credence.R;
import com.example.credence.UpdateActivity;
import com.example.credence.model;

import java.util.ArrayList;

public class RecyclerViewAdapter extends RecyclerView.Adapter<RecyclerViewAdapter.ViewHolder>{

    private Context context;
    private ArrayList<model> credences;

    public RecyclerViewAdapter(Context context, ArrayList<model> credences) {
        this.context = context;
        this.credences = credences;
    }

    @NonNull
    @Override
    public RecyclerViewAdapter.ViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View view = LayoutInflater.from(parent.getContext()).inflate(R.layout.row,parent,false);

        return new ViewHolder(view);
    }

    @Override
    public void onBindViewHolder(@NonNull final RecyclerViewAdapter.ViewHolder holder, int position) {
        String belief = (String) credences.get(position).getBelief();
        float per = (float) credences.get(position).getPer();



        holder.beliefT.setText(belief);
        holder.perT.setText(per+" %");
        holder.beliefT.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(view.getContext(), EditActivity.class);
                int id = holder.getAdapterPosition()+1;
                intent.putExtra("ID",String.valueOf(id));
                view.getContext().startActivity(intent);


            }
        });
        holder.perT.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(view.getContext(), EditActivity.class);
                int id = holder.getAdapterPosition()+1;
                intent.putExtra("ID",String.valueOf(id));
                view.getContext().startActivity(intent);


            }
        });
        holder.update_main.setOnClickListener(new View.OnClickListener() {
            @SuppressLint("ResourceAsColor")
            @Override
            public void onClick(View view) {
                Intent intent1 = new Intent(context, UpdateActivity.class);
                int id = holder.getAdapterPosition()+1;
                intent1.putExtra("ID",String.valueOf(id));
                context.startActivity(intent1);
                holder.update_main.setBackgroundColor(context.getResources().getColor(R.color.white));

            }
        });

    }

    @Override
    public int getItemCount() {
        return credences.size();
    }
    public class ViewHolder extends RecyclerView.ViewHolder implements View.OnClickListener{
        public TextView beliefT;
        public TextView perT;
        public Button update_main;

        public ViewHolder(@NonNull View itemView) {
            super(itemView);
            itemView.setOnClickListener(this);

            beliefT = itemView.findViewById(R.id.beliefT);
            perT = itemView.findViewById(R.id.perT);
            update_main = itemView.findViewById(R.id.update_main);
//            beliefT.setOnClickListener(this);
//            update_main.setOnClickListener(this);


        }

        @Override
        public void onClick(View view) {
//            beliefT.setOnClickListener(new View.OnClickListener() {
//                @Override
//                public void onClick(View view) {
//                    Intent intent = new Intent(view.getContext(), EditActivity.class);
//                    int id = getAdapterPosition()+1;
//                    intent.putExtra("ID",String.valueOf(id));
//                    view.getContext().startActivity(intent);
//
//                }
//            });
//            update_main.setOnClickListener(new View.OnClickListener() {
//                @SuppressLint("ResourceAsColor")
//                @Override
//                public void onClick(View view) {
//                    Intent intent1 = new Intent(context, UpdateActivity.class);
//                    int id = getAdapterPosition()+1;
//                    intent1.putExtra("ID",String.valueOf(id));
//                    context.startActivity(intent1);
//                    update_main.setBackgroundColor(context.getResources().getColor(R.color.white));
//
//                }
//            });


        }
    }
}

